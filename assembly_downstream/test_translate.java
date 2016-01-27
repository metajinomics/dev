import java.io.*;
import java.util.*;
import utils.*;

class test_translate{
    public static void main(String[] args){
	StringTranslator tran = new StringTranslator("!0", "lo");
	System.out.println(tran.translate("He!!0 W0r!d")); 

	String input="AliveisAwesome";
	StringBuilder input1 = new StringBuilder();
	input1.append(input);
	input1=input1.reverse(); 
	String th = input1.toString();
	System.out.println(th);
    }
}