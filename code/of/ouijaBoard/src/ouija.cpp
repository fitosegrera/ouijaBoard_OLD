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
	}
	while(receiver.hasWaitingMessages()){
	 	ofxOscMessage m;
        receiver.getNextMessage( &m );
        cout<< "New Message!" << endl;
        argument = m.getArgAsString(0);
        if ( argument == "H" ){
        	drawOuija = true;
        }
	 }
	//ofDrawBitmapString(title, ofGetWidth()/2, ofGetHeight()/5);
}
//--------------------------------------------------------------