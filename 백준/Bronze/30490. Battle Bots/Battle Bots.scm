(define (loop n c)
  (cond ((> n (expt 2 c)) (+ 1 (loop n (+ c 1))))
        (else 1)))
(print (loop (read) 0))