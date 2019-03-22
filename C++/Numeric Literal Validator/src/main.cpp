#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool isValid(string file_name,string line){

    bool valid = false; //flag
    int i = 0; //index
    
    //Move position by position through the string while changing the flag to true or false depending on the criteria read
            if(line[0] == '+'||line[0]=='-'){
                valid = false;
                i++;
                if (isdigit(line[i])){
                    valid = true;
                    i++;
                    while(isdigit(line[i]))
                    {
                        valid = true;
                        i++;
                    }
                    if ((isalpha(line[i]))&& (line[i]!= 'e'&& line[i]!='E')){
                    valid = false;
                    return false;}

                    if (line[i]=='.')
                    {
                        valid = false;
                        i++;
                        while (isdigit(line[i]))
                               {
                               valid = true;
                               i++;
                               }
                        if (line[i] == '.'){
                            valid = false;
                            return valid;
                        }
                    }
                    if (line[i]=='e'||line[i]=='e'){
                        valid = false;
                        i++;
                        if(line[i] == '+'||line[i]=='-'){
                            valid = false;
                            i++;}
                        while(isdigit(line[i])){
                            valid = true;
                            i++;
                            }
                        if ((isalpha(line[i]))){
                            valid = false;
                            return false;}
                        if (line[i] == '+'|| line[i] == '-'||line[i] == '.'){
                            valid = false;
                            return valid;
                            }
                        }
                    }
                if (line[i]=='.'){
                    valid = false;
                    i++;
                    if (!isdigit(line[i])){
                        return false;
                    }
                    while (isdigit(line[i])){
                        valid = true;
                        i++;
                    }
                    if ((isalpha(line[i]))&& (line[i]!= 'e'&& line[i]!='E')){
                    valid = false;
                    return false;}
                    if (line[i]=='.'){
                        valid = false;
                        return valid;
                    }
                    if (line[i]== 'e'|| line[i] == 'E'){
                        valid = false;
                        i++;
                        if (line[i] =='+'||line[i]=='-'){
                            valid = false;
                            i++;
                        }
                        while (isdigit(line[i])){
                        valid = true;
                        i++;
                    }
                }
                }
                if(line[i] == 'e'||line[i]=='E'){
                    valid = false;
                }
                return valid;}

            if(isdigit(line[0])){
                valid = true;
                i++;
                while(isdigit(line[i])){
                    valid = true;
                    i++;
                }
                if ((isalpha(line[i]))&& (line[i]!= 'e'&& line[i]!='E')){
                    valid = false;
                    return false;

                }
                if (line[i] == '+'||line[i] == '-'){
                    valid = false;
                    return valid;
                }
                if (line[i] == '.'){
                    valid = true;
                    i++;
                    while(isdigit(line[i])){
                        valid = true;
                        i++;
                    }
                    if(line[i] == '.'){
                        valid = false;
                        return valid;
                    }
                    if (line[i] == 'e'||line[i] == 'E'){
                        valid = false;
                        i++;
                        if (line[i] == '+'||line[i] == '-'){
                            valid = false;
                            i++;
                        }
                        if (isdigit(line[i])){
                            valid = true;
                            i++;
                            while (isdigit(line[i])){
                                valid = true;
                                i++;
                            }
                        if ((isalpha(line[i]))){
                            valid = false;
                            return false;}
                            if (line[i] == '+'|| line[i] == '-'||line[i] == '.'){
                            valid = false;
                            return valid;
                        }
                    }
                }
            }
            }

            else if(line[0] == '.'){
                valid = false;
                i++;
                if (line[i] == '+'||line[i] =='-'){
                    valid = false;
                    return valid;
                }
                if (isdigit(line[i])){
                    valid = true;
                    i++;
                    while (isdigit(line[i])){
                        valid = true;
                        i++;
                    }

                    if ((isalpha(line[i]))&& (line[i]!= 'e'&& line[i]!='E')){
                    valid = false;
                    return false;}

                    if (line[i]=='e'||line[i]=='E'){
                        valid = false;
                        i++;
                        if (line[i] == '+'||line[i] == '-'){
                            valid = false;
                            i++;
                        }
                        if (isdigit(line[i])){
                            valid = true;
                            i++;
                            while (isdigit(line[i])){
                                valid = true;
                                i++;
                            }
                            if (line[i] == '+'|| line[i] == '-'||line[i] == '.'||line[i] == 'e' || line[i] == 'E'||isalpha(line[i])){
                                valid = false;
                                return valid;
                                }
                        }
                    }
                }
                if (line[i] == '.'){
                    valid = false;
                    return valid;
                }
                if (line[i] == 'e'|| line[i] == 'E'){
                    valid = false;
                    return valid;
                }
            else if(line[0] == 'e'|| line[0] == 'E'){
                 valid = false;
                 return valid;
            }
            }
            return valid;
        }

int main()
{

    ifstream file;
    ofstream results;
    string line;
    string file_name;
    string r_file_name;
    cout << "Input text file name with file type (ex. test.txt): ";
    cin >> file_name;
    cout << "Input file name and file type to store results to: ";
    cin >> r_file_name;
    file.open(file_name);
    results.open(r_file_name);
    if(file.is_open()){
        while(getline(file,line)){
            if (isValid(file_name, line)){
                results << line + " valid \n";
            }
            else{
                results << line + " invalid \n";
            }
        }
        file.close();
        results.close();
    }
    else{
        cout << "could not open file" << endl;
    }



    return 0;
}
