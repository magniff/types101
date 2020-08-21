# Simple bidirectional type checker written in Python
This code is heavily inspired by the [Dave's talk](https://www.youtube.com/watch?v=utyBNDj7s2w) and it's corresponding implementation in Haskell.
Also, have a look on the Dave's STLC [tutorial](http://www.davidchristiansen.dk/tutorials/bidirectional.pdf).

# Formalities
## R-{True,False}
Typing relation for the boolean literals is an axiom, so we can `infere` it:

<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\emptyset} {\textbf{\Gamma} \vdash true \Rightarrow Boolean}">
<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\emptyset} {\textbf{\Gamma} \vdash false \Rightarrow Boolean}">

## R-Var
We are only allowed to get the type of a plain variable from the typing context, no guessing here

<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {(x : \tau) \in \textbf{\Gamma}} {\textbf{\Gamma} \vdash x \Rightarrow \tau}">

## R-Ann
If the variable is already annotated with a type, then let us just use this type, not forgeting to check it's consistency

<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\textbf{\Gamma} \vdash x \Leftarrow \tau} {\textbf{\Gamma} \vdash (x : \tau) \Rightarrow \tau}">

## R-Condition
<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\textbf{\Gamma} \vdash e_1 \Leftarrow Boolean \:\:\: \textbf{\Gamma} \vdash e_2 \Leftarrow \tau \:\:\: \textbf{\Gamma} \vdash e_3 \Leftarrow \tau} {\textbf{\Gamma} \vdash if\:e_1\:then\:e_2\:else\:e_3 \Leftarrow \tau}">

## R-Abstraction
<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\textbf{\Gamma}, x: \tau_1 \vdash t \Leftarrow \tau_2} {\textbf{\Gamma} \vdash \lambda x . t \Leftarrow \tau_1 \longrightarrow \tau_2}">

## R-Application
<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\textbf{\Gamma} \vdash t_1 \Rightarrow \tau_1 \longrightarrow \tau_2 \:\:\: \textbf{\Gamma} \vdash t_2 \Leftarrow \tau_1} {\textbf{\Gamma} \vdash t_1 \:\: t_2 \Rightarrow \tau_2}">

## R-Turnaround
<img src="https://render.githubusercontent.com/render/math?math=\Large \frac {\textbf{\Gamma} \vdash t \Rightarrow \tau} {\textbf{\Gamma} \vdash t \Leftarrow \tau}">
