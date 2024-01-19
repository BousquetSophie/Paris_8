%{
  open Ast
  open Ast.Syntax
%}

%token <int> Lint
%token <bool> Lbool
(*%token <string> Lstring*)
%token <string> Lvar
%token <Ast.type_t> Ldecl
%token Ladd Lsub Lmul Ldiv Lmod Loacc Lcacc Lopar Lcpar
%token Lprinti Lprintb Lgeti
%token Land Lor Lxor Lnot
%token Linf Lsup Linfe
%token Lreturn Lif Lelse Lloop Lassign Lsc Lend

%left Ladd Lsub
%left Lmul Ldiv Lmod
%left Lnot Land Lor Lxor
%left Lsup Linf Linfe
%left Lprinti Lprintb

%start prog

%type <Ast.Syntax.block> prog
%type <Ast.Syntax.block> block

%%

prog:
  | Lend { [] }
  | i = instr; b = prog { i :: b }
;

block:
  | i = instr; b = block { i :: b }
  | { [] }
;

instr:
  | Lreturn; e = expr; Lsc { Return { expr = e ; pos = $startpos($1) } }
  | t = Ldecl; v = Lvar; Lsc { Decl {name = v; type_t = t; pos = $startpos}}
  | v = Lvar; Lassign ; n = expr; Lsc {Assign { var = v; expr = n; pos = $startpos } }
  | Lif; e = expr; Loacc; a = block; Lcacc; Lelse; Loacc; b = block; Lcacc {Cond {expr = e; b1 = a; b2 = b; pos = $startpos}}
  | Lloop; e = expr; Loacc; a = block; Lcacc {Loop {expr = e; b = a; pos = $startpos}}
;

expr:
| n = Lint { Int { value = n ; pos = $startpos(n) }}
| b = Lbool { Bool { value = b ; pos = $startpos(b) }}
(*| s = Lstring { Str { value = s ; pos = $startpos(s) }}*)
| a = expr; Ladd; b = expr  { Call { func = "_add"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Lmul; b = expr  { Call { func = "_mul"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Ldiv; b = expr  { Call { func = "_div"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Lsub; b = expr  { Call { func = "_sub"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Lmod; b = expr  { Call { func = "_mod"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Land; b = expr  { Call { func = "_and"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Lor;  b = expr  { Call { func = "_or"; args =  [ a ; b ];  pos = $startpos } }
| a = expr; Lxor; b = expr  { Call { func = "_xor"; args = [ a ; b ];  pos = $startpos } }
| Lnot; a = expr  { Call { func = "_not"; args = [ a ];  pos = $startpos } }
| Lprinti; a = expr { Call { func = "_puti"; args = [ a ];  pos = $startpos } }
| Lprintb; a = expr { Call { func = "_putb"; args = [ a ];  pos = $startpos } }
| Lgeti { Call { func = "_geti"; args = [  ];  pos = $startpos } }
| a = expr; Linf; b = expr  { Call { func = "_inf"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Linfe; b = expr  { Call { func = "_infegal"; args = [ a ; b ];  pos = $startpos } }
| a = expr; Lsup; b = expr  { Call { func = "_sup"; args = [ a ; b ];  pos = $startpos } }
| v = Lvar { Var  { name = v; pos = $startpos } }
| Lopar; e = expr; Lcpar    { e }
;
