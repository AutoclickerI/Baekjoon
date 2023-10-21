(define (sum N A)
  (if (= N 0) 0 (+ (quotient (read) A) (sum (- N 1) A))))
(print (sum (read) (read)))