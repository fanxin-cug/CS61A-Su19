(define (sum lst)
    (define (sum-helper lst res)
        (if (null? lst)
            res
            (sum-helper (cdr lst) (+ (car lst) res))))
    (sum-helper lst 0))

(define (fib n)
    (define (fib-sofar n prev_1 prev_2)
        (if (= n 0)
            prev_2
        (fib-sofar (- n 1)  prev_2 (+ prev_1 prev_2))))
    (fib-sofar n 1 0))

(define (reverse lst)
    (define (reverse-sofar lst lst-sofar)
        (if (null? lst) 
            lst-sofar
            (reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
    (reverse-sofar lst '()))

(define (append a b)
    (define (rev-append-tail a b)
        (if (null? a)
            b
            (rev-append-tail (cdr a) (cons (car a) b))))
    (rev-append-tail (reverse a) b))

(define (insert n lst)
    (define (rev-insert lst rev-lst)
        (cond ((null? lst) (cons n rev-lst))
        ((> (car lst) n) (append (reverse lst) (cons n rev-lst)))
        (else (rev-insert (cdr lst) (cons (car lst) rev-lst)))))
    (reverse (rev-insert lst nil)))

(define-macro (make-lambda expr)
    `(lambda () ,expr))

(define (replicate x n)
    (if (= n 0) 
        nil
        (cons x (replicate x (- n 1)))))

(define-macro (repeat-n expr n)
    (cons 'begin (replicate expr (eval n))))

(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1
            ,expr2)))
