//this code add annotation (organism and function) at the end of the count table
// usage: java add_annotation.java normal_counts.txt mgm4675652.3_organism_KEGG.tab mgm4675652.3_function_KEGG.tab

import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
import java.lang.Object;
class add_annotation {
    public static void main(String[] args){
	//read organism then put in map
	HashMap <String,String> org = new HashMap<String,String>();
	File orFile = new File(args[1]);
	try{
	    Scanner orFile_scan = new Scanner(orFile);
	    while(orFile_scan.hasNextLine()){
		String line = orFile_scan.nextLine();
		String[] parts = line.split("\t");
		if (parts.length > 11){
		    org.put(parts[0],parts[12]);
		    //System.out.println(parts[12]);
		}
	    }
	}catch (FileNotFoundException e){
	    e.printStackTrace();
	}

	//read function then put in map
	HashMap <String,String> fun = new HashMap<String,String>();
        File funFile = new File(args[2]);
        try{
            Scanner funFile_scan = new Scanner(funFile);
            while(funFile_scan.hasNextLine()){
                String line = funFile_scan.nextLine();
                String[] parts = line.split("\t");
                if (parts.length > 11){
                    fun.put(parts[0],parts[12]);
                }
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }
	//read counts to process merge
	File countFile = new File(args[0]);
	try{
            Scanner coFile_scan = new Scanner(countFile);
	    PrintStream Result = new PrintStream(args[3]);
	    Result.println(coFile_scan.nextLine() + "\t" + "organism" +"\t" + "function");
            while(coFile_scan.hasNextLine()){
                String line = coFile_scan.nextLine();
		String[] parts = line.split("\t");
		String organism = "null";
		String function = "null";
		if(org.containsKey(parts[0])){
		    organism = org.get(parts[0]);
		}
		if(fun.containsKey(parts[0])){
		    function = fun.get(parts[0]);
		}
		Result.println(line + "\t" + organism +"\t" + function);
            }
	}catch (FileNotFoundException e){
            e.printStackTrace();
        }
	
    }
}