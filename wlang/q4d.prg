havoc x, y;
assume (x >= 0 and y >= 0);

r1 := x;
r2 := x;
c := y;
res := r1 * r2;


while c > 0
   inv (c >= 0  and  (r1 = x + (y - c)  and  (r2 = x - (y - c)  and  res = (x*x)-((y-c)*(y-c)))))
 do {
   r1 := r1 + 1;
   r2 := r2 - 1;
   res := r1 * r2;

   c := c - 1
};

assert (res = x*x - y*y)