method xSq_ySq__by__inc_dec_mul (x: nat, y: nat) returns (res: int)
  ensures res == x*x - y*y;
{
  var r1: int := x;
  var r2: int := x;
  var c: int := y;
  res := r1 * r2;

  while (c > 0)
    invariant c >= 0;
    invariant r1 == x + (y - c);
    invariant r2 == x - (y - c);
    invariant res == (x * x) - ((y-c) * (y-c));
    decreases c;
  {
    r1 := r1 + 1;
    r2 := r2 - 1;
    res := r1 * r2;
    
    c := c - 1;
  }
}
