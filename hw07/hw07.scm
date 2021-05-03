(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3) multiples-of-three))))

(define (rle s)
  (define (track-run elem st len)
    (cond ((null? st) (cons-stream (list elem len) nil))
      ((= elem (car st)) (track-run elem (cdr-stream st) (+ len 1)))
      (else (cons-stream (list elem len) (rle st)))))
  (if (null? s)
    nil
    (track-run (car s) (cdr-stream s) 1)))