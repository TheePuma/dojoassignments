functionFindprimes{
    var arr=[2,3,5]
    for(num=5;num<infinity;num++){
        for(i=0;i<arr.length;i++){
            if(num % arr[i] = 0){
                break;
            }
        }
        arr.push(num)
    }
    return arr;
}
