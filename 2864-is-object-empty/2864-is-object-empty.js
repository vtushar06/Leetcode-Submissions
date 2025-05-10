/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let keys=Object.keys(obj).map((item)=>item)
    if (keys.length===0){
        return true
    }
    else{
        return false
    }
    
};