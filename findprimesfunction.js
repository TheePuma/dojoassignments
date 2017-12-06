functionFindprimes{
    var arr=[2,3,5]
    var arr2=[2,3,5]
    for(num=5;num<infinity;num++){
        if(num > arr[arr2.length]*arr[arr2.length]){ //this line checks if num is greater than square of last value in 
            arr2.push(arr[arr2.length]) //
        }
        for(i=0;i<arr2.length;i++){
            if(num % arr2[i] = 0){
                break;
            }
        }
        arr.push(num)
    }
    return arr;
}

122424246
2
functionPrime(num){
    if(num is prime){
        return num, Prime(num+1)
    }
    return Prime(num+1)
}