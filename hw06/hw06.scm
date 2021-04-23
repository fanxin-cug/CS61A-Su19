; ;;;;;;;;;;;;;;
; ; Questions ;;
; ;;;;;;;;;;;;;;
; Scheme
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (unique s) 
    (if (null? s)
        nil
        (cons (car s) (filter (lambda (e) (not (equal? e (car s)))) (unique (cdr s))))))

(define (cons-all first rests) 
    (map (lambda (x) (cons first x)) rests))

; ; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond ((null? denoms) nil)
        ((= total 0) '(()))
        ((< total (car denoms)) (list-change total (cdr denoms)))
        (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))))

; Tail recursion
(define (replicate x n) 
    (define (replicate-helper x n res)
        (if (= n 0)
            res
            (replicate-helper x (- n 1) (append res (list x)))))
    (replicate-helper x n '()))

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))))

(define (accumulate-tail combiner start n term)
    (define (accumulate-helper combiner start n term res)
        (if (= n 0)
            res
            (accumulate-helper combiner start (- n 1) term (combiner (term n) res))))
    (accumulate-helper combiner start n term start))

; Macros
(define-macro
 (list-of map-expr for var in lst if filter-expr)
    ;(list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst)))
    `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst)))
