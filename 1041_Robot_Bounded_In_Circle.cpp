class Solution {
public:
     bool isRobotBounded(string instructions) {
        int xcoord = 0, ycoord = 0;
        int direc = 1;
        for(int j=0;j<4;j++){
            for(int i=0;i<instructions.size();i++){
                if(instructions[i] == 'G'){
                    switch(direc){
                        case 0: ycoord++;break;
                        case 2: ycoord--;break;
                        case 1: xcoord++;break;
                        case 3: xcoord--;break;
                    }
                }
                else{
                    direc += 4;
                    if(instructions[i] == 'R') direc++;
                    if(instructions[i] == 'L') direc--;
                    direc %= 4;
                }
            }
        }
        if(xcoord == 0 && ycoord == 0) return true;
        return false;
    }
};