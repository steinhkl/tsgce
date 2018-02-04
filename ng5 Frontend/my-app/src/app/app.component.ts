import {Component, OnInit, ViewChild} from '@angular/core';
import {MatButtonModule, MatCheckboxModule} from '@angular/material';
import {MatFormFieldModule} from '@angular/material/form-field';

import {HttpClientModule, HttpParams} from '@angular/common/http';
import {HttpClient, HttpHeaders} from '@angular/common/http';
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
  inputText = '';

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
  }

  send(): void {
    const body = 'sentence=' + this.inputText;
    console.log(this.inputText);
    this.http
      .post('http://localhost:8099', body, {
        responseType: 'text' /*there is a bug in ng5 it cant find the json session so we have to sue text*/

        /* headers: new HttpHeaders().set('Access-Control-Allow-Origin', '*')
             .set('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
             .set('Access-Control-Allow-Headers', 'Origin, Content-Type, X-Auth-Token')
             .set('Access-Control-Allow-Credentials', 'true'),
           /*params: new HttpParams().set('sentence', 'my name is what'),*/
      })
      .subscribe(data => {
          // Read the result field from the JSON response.
          //console.log("pure data")
          //console.log(data);
          const fields = data.split('Content-Type: application/json');

          const obj = JSON.parse(fields[1].toString());
          //console.log("oject")
          //console.log(obj);

          //console.log("only forms");
          //console.log(obj["forms"]);

          this.sentenceModels = obj["forms"];
          //sorts biggest api hits first
          this.sentenceModels.sort(function (obj1, obj2) {
            return obj2.APIhits - obj1.APIhits;
          });


        }
      );


  }


}
