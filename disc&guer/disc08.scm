(define (factorial x)
    (if (= x 0) 1 (* x (factorial (- x 1))))
)

(define (fib n)
    (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 2)) (fib (- n 1)))))
)

(define (my-append a b)
    (if (null? b) a
        (if (null? a) b
            (cons (car a) (my-append (cdr a) b))
        )
    )
)

(define (replicate x n)
    (if (= n 0) nil
        (cons x (replicate x (- n 1)))
    )
)

(define (uncompress s)
    (if (null? s) nil
        (my-append (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))
    )
)

(define (map fn lst)
    (if (null? lst) nil
        (cons (fn (car lst)) (map fn (cdr lst)))
    )
)

(define (deep-map fn nested-list)
    (cond
        ((null? nested-list) nil)
        ((number? nested-list) (fn nested-list))
        ((pair? (car nested-list)) (cons (deep-map fn (car nested-list)) (deep-map fn (cdr nested-list))))
        (else (cons (fn (car nested-list)) (deep-map fn (cdr nested-list))))
    )
)

(define (make-tree label branches) (cons label branches))

(define (label tree) (car tree))

(define (branches tree) (cdr tree))

(define (sum-lst lst)
    (if (null? lst) 0
        (+ (car lst) (sum-lst (cdr lst)))
    )
)

(define (tree-sum tree)
    (if (null? (branches tree))
        (label tree)
        (+ (label tree) (sum-lst (map tree-sum (branches tree))))
    )
)
