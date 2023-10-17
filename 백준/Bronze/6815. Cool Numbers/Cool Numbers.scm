(define (sum n s e)
  (let ((val (expt n 6))) (if (> val e) 0 (+ (or (and (>= val s) 1) 0) (sum (+ n 1) s e)))))
(print (sum 1 (read) (read)))