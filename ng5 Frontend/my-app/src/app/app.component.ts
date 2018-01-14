import {Component, OnInit, ViewChild} from '@angular/core';
import {MatButtonModule, MatCheckboxModule} from '@angular/material';
import {MatFormFieldModule} from '@angular/material/form-field';

import {HttpClientModule, HttpParams} from '@angular/common/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import {SentenceModel} from './sentence.model';
import {MatTableModule} from '@angular/material/table';


/*
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};*/

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'the NLP Grammar Checker';
  sentenceModels: SentenceModel[];
  inputText= '';

  constructor(private http: HttpClient) {}

  ngOnInit() {
  }

   send(): void {
    const body = 'sentence=' + this.inputText;
    console.log(this.inputText);
    this.http
      .post('http://localhost:8099', body , {
        responseType: 'text' /*there is a bug in ng5 it cant find the json session so we have to sue text*/

     /* headers: new HttpHeaders().set('Access-Control-Allow-Origin', '*')
          .set('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
          .set('Access-Control-Allow-Headers', 'Origin, Content-Type, X-Auth-Token')
          .set('Access-Control-Allow-Credentials', 'true'),
        /*params: new HttpParams().set('sentence', 'my name is what'),*/
      })
      .subscribe(data => {
        // Read the result field from the JSON response.
        console.log("pure data")
        console.log(data);
          const fields = data.split('Content-Type: application/json');
          console.log("filed 1 fom data")
          console.log(fields[1]);
          console.log(decodeURI(fields[1]));
         // fields[1]= fields[1].replace("\\\"","")
          fields[1]=  fields[1].replace(new RegExp(/\"/, 'g'), "");
          fields[1]=  fields[1].replace(new RegExp(/\\/, 'g'), "\"");
          fields[1] = fields[1].replace(/(\r\n|\n|\r)/gm,"");
          //fields[1]= "{ \"forms\":"+ fields[1]+"}";
          console.log(fields[1]);

          //[["\"this is a test sentence\"", 17300], ["\"this be a test sentence\"", 0], ["\"this am a test sentence\"", 0], ["\"this are a test sentence\"", 0], ["\"this being a test sentence\"", 0], ["\"this was a test sentence\"", 0], ["\"this were a test sentence\"", 0], ["\"this been a test sentence\"", 0]]
          //const fields1 = fields[1];
          const obj = JSON.parse(fields[1].toString());
          console.log("oject")
          console.log(obj);


          this.sentenceModels = obj;

	//this.sentenceModels = new this.sentenceModels[10];
		console.log(obj[0][0]);
          for (let i = 0; i < obj.length; i++) {
	this.sentenceModels[i].sentence = obj[i][0];
	this.sentenceModels[i].googlehits = obj[i][1];
         //   this.sentenceModels.push(new SentenceModel(obj[i][0],obj[i][1]));
          }

          this.sentenceModels.sort(function(obj1, obj2) {
            // Ascending: first age less than the previous
            return  obj2.googlehits - obj1.googlehits;
          });

          console.log("sentence model");
          console.log(this.sentenceModels);
         /* const obj = JSON.parse("{"+fields.toString()+"}");
          console.log("filed one from field one ")
          console.log(fields);
          console.log("oject")
        console.log(obj);
          this.sentenceModels = obj['forms'];
          console.log(this.sentenceModels);*/
      }
        );




   /* // Make the HTTP request:
    this.http.get('http://localhost:4200').subscribe(data => {
      console.log('send get');
      // Read the result field from the JSON response.
      this.results = data['results'];
    }); */
  }

  /*title = 'app';
  clickMessage = '';
  private heroesUrl = 'localhost';  // URL to web api

 /* const body = {name: 'Brad'}; */

/*
  welcome: string;
  games: [{
    game: string,
    platform: string,
    release: string
  }];
  /*constructor() {
    this.welcome = 'Display List using ngFor in Angular 2';

    this.games = [{
      game : 'Deus Ex: Mankind Divided',
      platform: ' Xbox One, PS4, PC',
      release : 'August 23'
    },
      {
        game : 'Hue',
        platform: ' Xbox One, PS4, Vita, PC',
        release : 'August 23'
      },
      {
        game : 'The Huntsman: Winter\'s Curse',
        platform: 'PS4',
        release : 'August 23'
      },
      {
        game : 'The Huntsman: Winter\'s Curse',
        platform: 'PS4',
        release : 'August 23'
      }];
  }*/

  /*
  @ViewChild('f') form: any;


  onSubmit() {
    if (this.form.valid) {
      console.log('Form Submitted!');
      this.form.reset();
    }
  }

  doPOST() {
    console.log('POST');
    const url = `localhost`;
    const search = new URLSearchParams();
    search.set('foo', 'moo');
    search.set('limit', '25');
    this.http.post(url, {moo: 'foo', goo: 'loo'}, {search}).subscribe(res => console.log(res.json()));
  }

  /*addHero(newHero: string) {
    if (newHero) {
      console.log('test');
    }
  }*/


/*
doPOST() {
  console.log('POST');
  this.http.post(this.heroesUrl, {moo: 'foo', goo: 'loo'}).subscribe(res => console.log(res.json()));
}
*/


  /*onClickMe() {
    this.clickMessage = 'You are my hero!';
  }*/

}
