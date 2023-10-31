(define (dectobin n)
  (if (= n 1) 1 (+ (remainder n 2) (* 10 (dectobin (quotient n 2))))))
(print (dectobin (read)))