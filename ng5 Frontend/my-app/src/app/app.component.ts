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
  title = 'app';
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
        console.log(data);
          const fields = data.split('Content-Type: application/json');
          console.log(fields[1]);
          const fields1 = fields[1];
          const obj = JSON.parse(fields1);
          console.log(fields1);
          this.sentenceModels = obj['forms'];
      console.log(this.sentenceModels);
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
