//
//
// ouija.cpp
// Created by fito_segrera
//
//

#include "ouija.h"
//--------------------------------------------------------------
void ouija::setupBoard(){
	ofBackground(0);
	
	drawOuija = false;
	drawH = false;
	drawI = false;
	drawT = false;
	drawL = false;
	drawE = false;
	drawR = false;
		
	boardImgBg.loadImage("bg.png");
	boardImgOuija.loadImage("OUIJA.png");
	boardImgH.loadImage("H.png");
	boardImgI.loadImage("I.png");
	boardImgT.loadImage("T.png");
	boardImgL.loadImage("L.png");
	boardImgE.loadImage("E.png");
	boardImgR.loadImage("R.png");

	cout << "listening for osc messages on port " << PORT << "\n";
	receiver.setup(PORT);

}

//--------------------------------------------------------------
void ouija::drawBoard(string title){
	boardImgBg.draw(0,0);
	if(drawOuija == true){
		boardImgOuija.draw(0,0);
	}else if (drawH == true){
		boardImgH.draw(0,0);
	}
	while(receiver.hasWaitingMessages()){
	 	ofxOscMessage m;
        receiver.getNextMessage( &m );
        cout<< "New Message!" << endl;
        //argument = m.getArgAsString(0);
        if ( m.getAddress() == "/OUIJA" ){
        	drawOuija = true;
        }else if ( m.getAddress() == "/H" ){
        	drawH = true;
        }/*if ( argument == "I" ){
        	drawI = true;
        }if(argument == "T" ){
        	drawT = true;
        }if ( argument == "L" ){
        	drawL = true;
        }if ( argument == "E" ){
        	drawE = true;
        }if ( argument == "R" ){
        	drawR = true;
        }*/
		//ofDrawBitmapString(title, 0, ofGetHeight() - 20);
	 }
}
//--------------------------------------------------------------
