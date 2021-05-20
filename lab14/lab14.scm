; Lab 14: Final Review

(define (compose-all funcs)
  (lambda (x)
    (if (null? funcs)
      x
      ((compose-all (cdr funcs)) ((car funcs) x))))
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  'YOUR-CODE-HERE
  (cond ((null? lst) #f)
    ((eq? (car lst) s) #t)
    (else (contains? (cdr lst) s)))
)