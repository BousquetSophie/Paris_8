open Ast.IR
open Mips

module Env = Map.Make(String)

type cinfo = { code: Mips.instr list
             ; env: Mips.loc Env.t
             ; fpo: int
             ; counter: int
             ; return: string }

let rec compile_expr e env =
  match e with
  | Int n   -> [ Li (V0, n) ]
  | Bool b  -> [ Li (V0, if b then 1 else 0) ]
  | Var v   -> [ Lw (V0, Env.find v env)]
  (*| Str s -> [ La (V0, Lbl s)]*)
  | Call (f, args) ->
     let ca = List.rev_map (fun a ->
                  compile_expr a env
                  @ [ Addi (SP, SP, -4)
                    ; Sw (V0, Mem (SP, 0)) ])
                args in
     List.flatten ca
     @ [ Jal f
       ; Addi (SP, SP, 4 * (List.length args)) ]

let rec compile_instr i info =
  match i with
    | Decl v ->
      { info with
        env = Env.add v (Mem (FP, -info.fpo)) info.env
      ; fpo = info.fpo + 4 }
    | Assign (v, e) ->
      { info with
        code = info.code
          @ compile_expr e info.env
          @ [Sw (V0, Env.find v info.env)]}
    | Return e -> 
      { info with
        code = info.code
        @ compile_expr e info.env
        (*@ print_int*)}
    | Cond (c, t, e) ->
      let uniq = string_of_int info.counter in
      let ct = compile_block t { info with code = []
                                  ; counter = info.counter + 1 } in
      let ce = compile_block e { info with code = []
                                  ; counter = ct.counter + 1 } in
        { info with
          code = info.code
            @ compile_expr c info.env
            @ [ Beqz (V0, "else" ^ uniq) ]
            @ ct.code
            @ [ B ("endif" ^ uniq)
              ; Label ("else" ^ uniq) ]
            @ ce.code
            @ [ Label ("endif" ^ uniq) ]
        ; counter = ce.counter }
    | Loop (c, t) ->
      let uniq = string_of_int info.counter in
      let ct = compile_block t { info with code = []
                                    ; counter = info.counter + 1 } in
        { info with
          code = info.code
            @ [ Label ("loop" ^ uniq)]
            @ compile_expr c info.env
            @ [ Beqz (V0, "endloop" ^ uniq) ]
            @ ct.code
            @ [ J ("loop" ^ uniq)]
            @ [ Label ("endloop" ^ uniq) ]
            @ [Jr RA]
          ; counter = ct.counter }

and compile_block b info =
  match b with
    | [] -> info
    | i :: r ->
      compile_block r (compile_instr i info)

      
let compile ir =
  let cinfo = compile_block ir { code = []
                                 ; env = Env.empty
                                 ; fpo = 8
                                 ; counter = 1
                                 ; return = "ret" ^ (string_of_int 1) } in
  { text = Baselib.builtins
  @ [ Label "main"
  ; Addi (SP, SP, -cinfo.fpo)
  ; Sw (RA, Mem (SP, cinfo.fpo - 4))
  ; Sw (FP, Mem (SP, cinfo.fpo - 8))
  ; Addi (FP, SP, cinfo.fpo - 4) ]
  @ cinfo.code 
  @ [ Addi (SP, SP, cinfo.fpo)
  ; Lw (RA, Mem (FP, 0))
  ; Lw (FP, Mem (FP, -4))
  ; Jr (RA) ]
  ; data = [] }
