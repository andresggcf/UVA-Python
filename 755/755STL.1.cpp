#include <iostream>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

char letraNum(char m){
	if(m == 'A' || m == 'B' || m == 'C'){
		return '2';
	}
	else if(m == 'D' || m == 'E' || m == 'F'){
		return '3';
	}
	else if(m == 'G' || m == 'H' || m == 'I'){
		return '4';
	}
	else if(m == 'J' || m == 'K' || m == 'L'){
		return '5';
	}	
	else if(m == 'M' || m == 'N' || m == 'O'){
		return '6';
	}	
	else if(m == 'P' || m == 'R' || m == 'S'){
		return '7';
	}
	else if(m == 'T' || m == 'U' || m == 'V'){
		return '8';
	}
	else if(m == 'W' || m == 'X' || m == 'Y'){
		return '9';
	}
	return m;
}


string cambio(string x){
    string r;
    char n;
	for(int a = 0; a < x.size(); a++){
		if(x[a] != '-'){
		   n = letraNum(x[a]);
		   r += n;
		}
	}
}


int main(){
	vector<string> num;
	int dataSet, i;
	string tel, g;
	cin >> dataSet;
	cout << " " << endl;
	for(int j = 0; j < dataSet; j++){
		cin >> i;
		for(int k = 0; k < i ; k++){
			cin >> tel;
			g = cambio(tel);
		}
	}
}