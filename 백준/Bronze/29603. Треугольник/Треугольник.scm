(define (printer p q r s t u)
  (print (- (+ p t) r) " " (- (+ q u) s))
  (print (- (+ p r) t) " " (- (+ q s) u))
  (print (- (+ r t) p) " " (- (+ s u) q)))
(printer (read) (read) (read) (read) (read) (read))
  