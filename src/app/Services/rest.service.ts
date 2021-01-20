import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Weather } from '../Weather';

@Injectable({
  providedIn: 'root'
})
export class RestService implements OnInit {

  constructor(private http : HttpClient) { }

  ngOnInit(){
  }

 

}
