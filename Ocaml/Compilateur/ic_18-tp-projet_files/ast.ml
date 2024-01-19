type type_t =
  | Int_t
  | Bool_t
  | Func_t of type_t * type_t list

let rec string_of_type_t t =
  match t with
  | Int_t  -> "int"
  | Bool_t -> "bool"
  | Func_t (r, a) ->
    (if (List.length a) > 1 then "(" else "")
      ^ (String.concat ", " (List.map string_of_type_t a))
      ^ (if (List.length a) > 1 then ")" else "")
      ^ " -> " ^ (string_of_type_t r)

module Syntax = struct
  type expr =
    | Int of { value: int
      ; pos: Lexing.position }
    | Bool of { value: bool
      ; pos: Lexing.position }
    | Var  of { name: string
      ; pos: Lexing.position }
    | Call of { func: string
      ; args: expr list
      ; pos: Lexing.position }
  type instr =
    | Decl   of { name: string
      ; type_t: type_t
      ; pos: Lexing.position }
    | Assign of { var: string
      ; expr: expr
      ; pos: Lexing.position }
    | Cond of { expr : expr
      ; b1: block
      ; b2: block
      ; pos: Lexing.position}
    | Loop of { expr : expr
      ; b: block
      ; pos: Lexing.position}
    | Return of { expr: expr
      ; pos: Lexing.position }
  and block = instr list
end

module IR = struct
  type expr =
    | Int of int
    | Bool of bool
    | Var  of string
    | Call of string * expr list
  type instr =
    | Decl   of string
    | Assign of string * expr
    | Cond of expr * block * block
    | Loop of expr * block
    | Return of expr
  and block = instr list
  type def =
    | Func of string * string list * block
end
