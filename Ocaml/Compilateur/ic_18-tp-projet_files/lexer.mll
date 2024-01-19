{
  open Lexing
  open Parser

  exception Error of char
}

let alpha = ['a'-'z' 'A'-'Z']
let num = ['0'-'9']
let identifier = alpha (alpha | num | '-' | '_')*

rule token = parse
| eof              { Lend }
| [ ' ' '\t' ]     { token lexbuf }
| '\n'             { new_line lexbuf; token lexbuf }
| ';'              { Lsc }
| '('              { Lopar }
| ')'              { Lcpar }
| '{'              { Loacc }
| '}'              { Lcacc }
| num+ as n        { Lint (int_of_string n) }
(*| alpha+ as s { Lstring (s) }*)
| "true"           { Lbool (true)}
| "false"          { Lbool (false)}
| '+'              { Ladd }
| '-'              { Lsub }
| '*'              { Lmul }
| '/'              { Ldiv }
| '%'              { Lmod }
| "&&"             { Land }
| "||"             { Lor }
| '^'              { Lxor }
| '!'              { Lnot }
| '<'              { Linf }
| "<="             { Linfe }
| '>'              { Lsup }
| "return"         { Lreturn }
| "int"            { Ldecl (Int_t)}
| "bool"           { Ldecl (Bool_t)}
| '='              { Lassign }
| "if"             { Lif }
| "else"           { Lelse }
| "while"          { Lloop }
| "printi"         { Lprinti }
| "printb"         { Lprintb }
| "scani"          { Lgeti }
| identifier as v  { Lvar (v)}
| _ as c           { raise (Error c) }
