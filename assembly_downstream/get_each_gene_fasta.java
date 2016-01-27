//java get_each_gene_fasta.java assembly 350.faa output.fna

import java.io.*;
import java.util.*;
import utils.*;
class get_each_gene_fasta {
    public static void main(String[] args){
	if(args.length != 3) {
	    System.err.println("usage: java get_each_gene_fasta assembly 350.faa output.fna");
	    System.exit(0);
	}
	
	//read assembly to put into hash map

	//System.exit(0);
	HashMap <String,String> assem = new HashMap<String,String>();
	File assemFile = new File(args[0]);
	try{
	    Scanner assemFile_scan = new Scanner(assemFile);
	    while(assemFile_scan.hasNextLine()){
		String line = assemFile_scan.nextLine();
		String[] parts = line.split(" ");
		String seq = assemFile_scan.nextLine();
		//System.out.println(parts[0]);
		assem.put(parts[0],seq);
	    }
	}catch (FileNotFoundException e){
	    e.printStackTrace();
	}

	//read 350.faa to find seq then write
	//expected sequence name has one under bar such as  k99_1 
	StringTranslator tran = new StringTranslator("AGCTagct", "TCGAtcga");
	File faaFile = new File(args[1]);
	try{
	    PrintStream Result = new PrintStream(args[2]);
	    Scanner faaFile_scan = new Scanner(faaFile);
	    while(faaFile_scan.hasNextLine()){
		String line = faaFile_scan.nextLine();
		String[] parts = line.split("_");
		String id = parts[0]+"_"+parts[1];
		int start = Integer.parseInt(parts[2]);
		int end = Integer.parseInt(parts[3]);
		String direc = parts[4];
		String temp = assem.get(id);
		// if reverse direction then get reverse compliment
		if(direc.equals("-")){
		    temp = tran.translate(temp);
		    StringBuilder input1 = new StringBuilder();
		    input1.append(temp);
		    input1 = input1.reverse();
		    temp = input1.toString();
		}
		Result.println(line);
		Result.println(temp.substring(start,end));
		faaFile_scan.nextLine();
	    }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }
    }
}