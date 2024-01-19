open Ast
open Mips

module Env = Map.Make(String)

let _types_ =
  Env.of_seq
    (List.to_seq
       [ "_add", Func_t (Int_t, [ Int_t ; Int_t ])
       ; "_sub", Func_t (Int_t, [ Int_t ; Int_t ])
       ; "_mul", Func_t (Int_t, [ Int_t ; Int_t ])
       ; "_div", Func_t (Int_t, [ Int_t ; Int_t ])
       ; "_mod", Func_t (Int_t, [ Int_t ; Int_t ])
       ; "_and", Func_t (Bool_t, [ Bool_t ; Bool_t ])
       ; "_or",  Func_t (Bool_t, [ Bool_t ; Bool_t ])
       ; "_xor", Func_t (Int_t, [ Int_t ; Int_t ])
       ; "_not", Func_t (Bool_t, [ Bool_t])
       ; "_puti", Func_t (Int_t, [ Int_t])
       ; "_putb", Func_t (Int_t, [ Bool_t])
       ; "_geti", Func_t (Int_t, [ ])
       ; "_inf", Func_t (Bool_t, [ Int_t ; Int_t ])
       ; "_infegal", Func_t (Bool_t, [ Int_t ; Int_t ])
       ; "_sup", Func_t (Bool_t, [ Int_t ; Int_t ])
    ])

let builtins = [
  Label "_add"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Add (V0, T0, T1)
  ; Jr RA

  ; Label "_sub"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Sub (V0, T0, T1)
  ; Jr RA

  ; Label "_mul"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Mul (V0, T0, T1)
  ; Jr RA

  ; Label "_div"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Div (V0, T0, T1)
  ; Jr RA

  ; Label "_and"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; And (V0, T0, T1)
  ; Jr RA

  ; Label "_or"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Or (V0, T0, T1)
  ; Jr RA

  ; Label "_xor"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Xor (V0, T0, T1)
  ; Jr RA

  ; Label "_not"
  ; Lw (T0, Mem (SP, 0))
  ; Nor (V0, T0, 0)
  ; Jr RA

  ; Label "_mod"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Div (T2, T0, T1)
  ; Mfhi V0
  ; Jr RA

  ; Label "_puti"
  ; Lw (A0, Mem (SP, 0))
  ; Li (V0, 1)
  ; Syscall
  ; Jr RA

  ; Label "_putb"
  ; Lw (A0, Mem (SP, 0))
  ; Li (V0, 1)
  ; Syscall
  ; Jr RA

  ; Label "_geti"
  ; Lw (A0, Mem (SP, 0))
  ; Li (V0, 5)
  ; Syscall
  ; Jr RA

  ; Label "_inf"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Slt (V0, T0, T1)
  ; Jr RA

  ; Label "_sup"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Sgt (V0, T0, T1)
  ; Jr RA

  ; Label "_infegal"
  ; Lw (T0, Mem (SP, 0))
  ; Lw (T1, Mem (SP, 4))
  ; Sle (V0, T0, T1)
  ; Jr RA
]
