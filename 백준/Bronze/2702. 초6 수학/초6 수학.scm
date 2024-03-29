(define (print p q)
  (display p)
  (display " ")
  (display q)
  (newline))
(define (gcd a b)
  (cond ((= (remainder a b) 0) b)
        (else (gcd b (remainder a b)))))
(define (loop n)
  (cond ((= n 0) 0)
        (else (let ((p (read)) (q (read)))
          (print (/ (* p q) (gcd p q)) (gcd p q))) (loop (- n 1)))))
(loop (read))