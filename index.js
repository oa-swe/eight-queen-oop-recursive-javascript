class queen {
    constructor(x,y){
        this.x=x;
        this.y=y;
    }
    coincide(xx,yy){
        var xd= Math.abs(xx-this.x);
        var yd= Math.abs(yy-this.y);
        if(xd===yd) return true;
        if(this.x==xx || this.y==yy) return true;
        return false;
    }
}
class board {
    queens=[];
    addQueen(x,y){
        var newQ= new queen(x,y);
        for(var i=0;i<this.queens.length;i++){
            var olderQ = this.queens[i];
            if(newQ.coincide(olderQ.x,olderQ.y)){
                return false;
            }
        }
        this.queens.push(newQ);
        return true;
    }
    pickItUp(){
        this.queens.pop();
    }
}
const myBoard = new board();
function putQueenOnBoard(col){
    var put=false;
    for(var i=1;i<9;i++){
        if(myBoard.addQueen(col,i)){
            put=true;
            if(col==8){
                console.log(myBoard);
            }else{
                putQueenOnBoard(col+1);
            }
        }
        if(put){
            myBoard.pickItUp(col);
            put=false;
        }
    }
}
putQueenOnBoard(1);