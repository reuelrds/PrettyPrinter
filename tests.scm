((lambda (x y . z) z)3 4 5 6)
(lambda (y) (+ x y))
((lambda (x) (+ x x)) 4)
(define add4(let ((x 4))(lambda (y) (+ x y))))
(define (fac n) (lambda (x) (+ x x)) 4)
(define (fac n)(define (f g n x)(if (= n 0) x (g g (- n 1) (* n x))))  (f f n 1))