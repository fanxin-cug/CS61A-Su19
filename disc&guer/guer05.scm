(define (cat meow purr) (+ meow purr))
(define cat (lambda (meow purr) (+ meow purr)))

(define (sum-every-other lst)
    (cond ((null? lst) 0)
        (else (+ (car lst)
        (sum-every-other (cdr lst))))))

(define (sixty-ones lst)
    (cond ((or (null? lst) (null? (cdr lst))) 0)
        ((and (= (car lst) 6) (= (car (cdr lst)) 1)) (+ 1 (sixty-ones (cdr (cdr lst)))))
        (else (sixty-ones (cdr lst)))))


(define (cons-all first rests) 
    (map (lambda (x) (cons first x)) rests))
(define (no-elevens n)
    (cond ((= n 0) '(()))
        ((= n 1) '((6) (1)))
        (else (filter (lambda (x) (not (and (= (car x) 1) (= (car (cdr x)) 1))))
        (append (cons-all 6 (no-elevens (- n 1))) (cons-all 1 (no-elevens (- n 1))))))))

(define (remember f)
    (lambda () (if (procedure? f) (set! f (f)) f))

(define (my-append a b)
    (if (null? a) b
        (cons (car a) (my-append (cdr a) b))))
(define (concat lsts)
    (if (null? lsts) nil
        (my-append (car lsts) (concat (cdr lsts)))))

(define (better-append x . y)
    (concat (cons x y)))

(define (mult x y)
    (define (mult-helper x y res)
        (if (= 0 y) res
        (mult-helper x (- y 1) (+ x res))))
    (mult-helper x y 0))

(define (true1 n)
    (define (true1-helper n res)
        (if (= n 0)
            res
            (true1-helper (- n 1) (and #t res))))
    (true1-helper n #t))

(define (true2 n)
    (define (true2-helper n res)
        (if (= n 0)
            res
            (true2-helper (- n 1) (or #f res))))
    (true2-helper n #t))

(define (contains lst x)
    (cond ((null? lst) #f)
        ((equal? (car lst) x) #t)
        (else (contains (cdr lst) x))))

(define (sum-satisfied-k lst f k)
    (define (sum-helper lst k res)
        (cond ((< (length lst) k) 0)
        ((= k 0) res)
        (else (sum-helper (cdr lst) (- k 1) (+ res (car lst))))))
    (sum-helper (filter f lst) k 0))

(define (remove-range lst i j)
    (define (remove-helper lst i j k res)
        (cond ((= k j) (append res (cdr lst)))
            ((< k i) (remove-helper (cdr lst) i j (+ k 1) (append res (list (car lst)))))
            (else (remove-helper (cdr lst) i j (+ k 1) res))))
    (remove-helper lst i j 0 nil))