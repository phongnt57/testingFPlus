function GiaiPTB2(a,b,c){
  var nghiem={};
  if(!isNaN(a) || !isNaN(b) || !isNaN(c)){
    if(a==0){
      if(b==0){
        if(c==0){
          nghiem.x='R';
          return nghiem;
        }
        return nghiem;
      }
      nghiem.x= -b/c;
      return nghiem;
    } else{
      var delta= b*b - 4*a*c;
      if(delta<0){
        return nghiem;
      }
      nghiem.x1= (-b + Math.sqrt(delta))/(2*a);
      nghiem.x2= (-b - Math.sqrt(delta))/(2*a);
      return nghiem;
    }
  }
  return nghiem;
}
