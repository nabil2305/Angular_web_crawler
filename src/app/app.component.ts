import { Component, OnInit } from '@angular/core';
import { RestService } from './Services/rest.service';
import { Weather } from './Weather';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'AngularFlask';
  userInput='india';

  constructor(private rs : RestService,private http : HttpClient){}

  headers = ["day","temperature", "windspeed",  "event"]

  weather : Weather[] = [];
  sol:[]=[];
  s_item:string="";

  ngOnInit()
  {

     
  }
  func()
  {
   this.http.post<any>('http://127.0.0.1:5000/starting', { 'item':this.s_item }).subscribe(data => {
      this.sol=data;
        console.log("sol="+data);
        console.log("sol length="+this.sol.length);

         })
     console.log("value searched");

    }
    reset()
    {
      this.sol=[];
      console.log("value reset");
    }
    generate()
    {
      this.http.get('http://127.0.0.1:5000/generate').subscribe(data=>{
        console.log("file generated");
        console.log(data);
      })
    }
}
