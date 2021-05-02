(define (map-stream f s)
    (if (null? s) 
        nil
        (cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define (slice s start end)
    (cond ((or (null? s) (= end 0)) nil)
        ((> start 0) (slice (cdr-stream s) (- start 1) (- end 1)))
        (else (cons (car s) (slice (cdr-stream s) (- start 1) (- end 1))))))

(define (filter-stream f s)
    (cond ((null? s) nil)
        ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s))))
        (else (filter-stream f (cdr-stream s)))))

(define (sift prime s)
    (filter-stream (lambda (x) (not (= 0 (modulo x prime)))) s))

(define (sieve s)
    (cons-stream (car s) (sieve (sift (car s) (cdr-stream s)))))

(define primes (sieve (naturals 2)))

(slice primes 0 10)

(define (combine-with f xs ys)
    (if (or (null? xs) (null? ys))
        nil
        (cons-stream (f (car xs) (car ys)) (combine-with f (cdr-stream xs) (cdr-stream ys)))))

(define factorials (cons-stream 1 (combine-with * (naturals 1) factorials)))

(define fibs (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))

(define (exp x)
    (let ((terms (combine-with (lambda (a b) (/ (expt x a) b))
        (cdr-stream (naturals 0)) (cdr-stream factorials))))
        (cons-stream 1 (combine-with + terms (exp x)))))

(define-macro (make-stream first second)
    `(list ,first (make-lambda ,second)))

(define (cdr-stream stream)
    ((car (cdr stream))))