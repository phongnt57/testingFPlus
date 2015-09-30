function evensum(array){
	var sum = 0;
	if(!Array.isArray(array)){
		return null;
	}
	for(var i =0 ; i< array.length; i++){
		if(array[i]%2 ==0){
			sum += array[i];
		}
	}
	return sum;
}