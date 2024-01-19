type reg =
  | Zero
  | SP
  | FP
  | RA
  | V0
  | A0
  | A1
  | T0
  | T1
  | T2
  | T3
  | T4

type label = string

type loc =
  | Lbl of label
  | Reg of reg
  | Mem of reg * int

type instr =
    | Label of label
    | Li    of reg * int
    | La    of reg * loc
    | Sw    of reg * loc
    | Lw    of reg * loc
    | Sb    of reg * loc
    | Lb    of reg * loc
    | Move  of reg * reg
    | Addi  of reg * reg * int
    | Add   of reg * reg * reg
    | Sub   of reg * reg * reg
    | Mul   of reg * reg * reg
    | Div   of reg * reg * reg
    | And   of reg * reg * reg
    | Or    of reg * reg * reg
    | Sgt   of reg * reg * reg
    | Slt   of reg * reg * reg
    | Sle   of reg * reg * reg
    | Xor   of reg * reg * reg
    | Nor   of reg * reg * int
    | Syscall
    | Mfhi  of reg
    | B     of label
    | Beq   of reg * reg * label
    | Beq2  of reg * int * label
    | Beqz  of reg * label
    | Bne   of reg * reg * label
    | Bgtu  of reg * reg * label
    | Bleu  of reg * int * label
    | Jal   of label
    | Jr    of reg
    | J     of label

type directive =
  | Asciiz of string

type decl = label * directive

type asm = { text: instr list ; data: decl list }

let ps = Printf.sprintf (* alias raccourci *)

let fmt_reg = function
  | Zero -> "$zero"
  | SP   -> "$sp"
  | FP   -> "$fp"
  | RA   -> "$ra"
  | V0   -> "$v0"
  | A0   -> "$a0"
  | A1   -> "$a1"
  | T0   -> "$t0"
  | T1   -> "$t1"
  | T2   -> "$t2"
  | T3   -> "$t3"
  | T4   -> "$t4"

let fmt_loc = function
  | Lbl (l)    -> ps "\"%s\"" l
  | Reg (r)    -> fmt_reg r
  | Mem (r, o) -> ps "%d(%s)" o (fmt_reg r)

let fmt_instr = function
  | Label (l)        -> ps "%s:" l
  | Li (r, i)        -> ps "  li %s, %d" (fmt_reg r) i
  | La (r, a)        -> ps "  la %s, %s" (fmt_reg r) (fmt_loc a)
  | Sw (r, a)        -> ps "  sw %s, %s" (fmt_reg r) (fmt_loc a)
  | Lw (r, a)        -> ps "  lw %s, %s" (fmt_reg r) (fmt_loc a)
  | Sb (r, a)        -> ps "  sb %s, %s" (fmt_reg r) (fmt_loc a)
  | Lb (r, a)        -> ps "  lb %s, %s" (fmt_reg r) (fmt_loc a)
  | Move (rd, rs)    -> ps "  move %s, %s" (fmt_reg rd) (fmt_reg rs)
  | Addi (rd, rs, i) -> ps "  addi %s, %s, %d" (fmt_reg rd) (fmt_reg rs) i
  | Add (rd, rs, rt) -> ps "  add %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Sub (rd, rs, rt) -> ps "  sub %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Mul (rd, rs, rt) -> ps "  mul %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Div (rd, rs, rt) -> ps "  div %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | And (rd, rs, rt) -> ps "  and %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Or (rd, rs, rt)  -> ps "  or %s, %s, %s"  (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Sgt (rd, rs, rt) -> ps "  sgt %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Slt (rd, rs, rt) -> ps "  slt %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Sle (rd, rs, rt) -> ps "  sle %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Xor (rd, rs, rt) -> ps "  xor %s, %s, %s" (fmt_reg rd) (fmt_reg rs) (fmt_reg rt)
  | Nor (rd, rs, i)  -> ps "  nor %s, %s, %d" (fmt_reg rd) (fmt_reg rs) i
  | Syscall          -> ps "  syscall"
  | Mfhi (r)         -> ps "  mfhi %s" (fmt_reg r)
  | B (l)            -> ps "  b %s" l
  | Beq (rs, rt, l)  -> ps "  beq %s, %s, %s" (fmt_reg rs) (fmt_reg rt) l
  | Beq2(rs, i, l)   -> ps "  beq %s, %d, %s" (fmt_reg rs) i l 
  | Beqz (rs, l)     -> ps "  beqz %s, %s" (fmt_reg rs) l
  | Bne (rs, rt, l)  -> ps "  bne %s, %s, %s" (fmt_reg rs) (fmt_reg rt) l
  | Bgtu (rs, rt, l) -> ps "  bgtu %s, %s, %s" (fmt_reg rs) (fmt_reg rt) l
  | Bleu (rs, i, l)  -> ps "  bleu %s, %d, %s" (fmt_reg rs) i l 
  | Jal (l)          -> ps "  jal %s" l
  | Jr (r)           -> ps "  jr %s" (fmt_reg r)
  | J (l)            -> ps "  j %s" l

let fmt_dir = function
  | Asciiz (s) -> ps ".asciiz \"%s\"" s

let print_int =
  [ Move (A0, V0)
  ; Li (V0, 1)
  ; Syscall ]

let print_string =
    [ Move (A0, V0)
    ; Li (V0, 4)
    ; Syscall ]

let emit oc asm =
  Printf.fprintf oc ".text\n.globl main\n" ;
  List.iter (fun i -> Printf.fprintf oc "%s\n" (fmt_instr i)) asm.text ;
  Printf.fprintf oc "\n.data\n" ;
  List.iter (fun (l, d) -> Printf.fprintf oc "%s: %s\n" l (fmt_dir d)) asm.data
