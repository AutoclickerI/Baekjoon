(define l '(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21))
(define (reverse l)
  (if (null? l) l (append (reverse (cdr l)) (list (car l)))))
(define (get-range l r lis)
  (cond ((< 1 l) (get-range (- l 1) (- r 1) (cdr lis)))
        ((= 1 l) (if (= r 0) '() (cons (car lis) (get-range l (- r 1) (cdr lis)))))))
(define (query p q l) 
  (append (get-range 1 (- p 1) l) 
          (append (reverse (get-range p q l)) (get-range (+ q 1) 21 l))))
(define (loop n l)
  (if (= n 0) l (loop (- n 1) (query (read) (read) l))))
(define (printer n l)
  (cond ((= n 0) 0)
        (else (display (car l)) (display " ") (printer (- n 1) (cdr l)))))
(printer 20 (loop 10 l))