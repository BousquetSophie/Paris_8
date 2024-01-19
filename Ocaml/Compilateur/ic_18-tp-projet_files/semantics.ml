open Ast
open Ast.IR
open Baselib

exception Error of string * Lexing.position

let expr_pos expr =
  match expr with
  | Syntax.Int i  -> i.pos
  | Syntax.Bool b  -> b.pos
  | Syntax.Var v -> v.pos
  | Syntax.Call c -> c.pos

let errt expected given pos =
  raise (Error (Printf.sprintf "expected %s but given %s"
                  (string_of_type_t expected)
                  (string_of_type_t given),
                pos))

let rec analyze_expr env expr =
  match expr with
  | Syntax.Int n -> Int n.value, Int_t
  | Syntax.Bool b -> Bool b.value, Bool_t
  | Syntax.Var v ->
     if Env.mem v.name env then
       Var v.name, Env.find v.name env
     else
       raise (Error (Printf.sprintf "unbound variable '%s'" v.name,
                     v.pos))
  | Syntax.Call c ->
    match Env.find_opt c.func env with
    | Some (Func_t (rt, at)) ->
       if List.length at != List.length c.args then
         raise (Error (Printf.sprintf "expected %d arguments but given %d"
                         (List.length at) (List.length c.args), c.pos)) ;
       let args = List.map2 (fun eat a -> let aa, at = analyze_expr env a
                                          in if at = eat then aa
                                          else errt eat at (expr_pos a)) at c.args in
       Call (c.func, args), rt
    | Some _ -> raise (Error (Printf.sprintf "'%s' is not a function" c.func,
                              c.pos))
    | None -> raise (Error (Printf.sprintf "undefined function '%s'" c.func,
                            c.pos))

let rec analyze_instr env instr =
  match instr with
    | Syntax.Decl d ->
      let nenv = Env.add d.name d.type_t env in Decl d.name, nenv
    | Syntax.Assign a ->
      (match Env.find_opt a.var env with
      | None -> raise (Error (Printf.sprintf "unbound variable'%s'" a.var, a.pos))
      | Some t -> let ae, et = analyze_expr env a.expr in
        if et = t then Assign (a.var, ae), env
        else errt t et (expr_pos a.expr))
    | Syntax.Cond c ->
      let condition, condition_type = analyze_expr env c.expr in
        if condition_type <> Bool_t then
          raise (Error ("L'expression doit être de type bool", expr_pos c.expr));
      let if_block = analyze_block c.b1 env in
      let then_block = analyze_block c.b2 env in 
      Cond (condition, if_block, then_block), env
    | Syntax.Loop l ->
      let condition, condition_type = analyze_expr env l.expr in
        if condition_type <> Bool_t then
          raise (Error ("L'expression doit être de type bool", expr_pos l.expr));
      let loop_block = analyze_block l.b env in 
      Loop (condition, loop_block), env
    | Syntax.Return r -> 
      let ae, _ = analyze_expr env r.expr in
      Return ae, env
and analyze_block block env =
  match block with
    | [] -> []
    | instr :: rest ->
      let ai, new_env = analyze_instr env instr in
      ai :: (analyze_block rest new_env)

let analyze parsed =
  analyze_block parsed Baselib._types_
