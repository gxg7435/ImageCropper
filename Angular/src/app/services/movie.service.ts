import {Injectable} from '@angular/core';
import {Jsonp} from '@angular/http';
import 'rxjs/Rx';
import {Http, Response} from "@angular/http";  
import {Observable} from "rxjs/Rx";

@Injectable()
export class MovieService {
    apikey:string;
    private searchURL:string;

    constructor(private _jsonp:Jsonp,private _http:Http){
        this.apikey = 'kqtwdcapd2a5hth6aqw4h65f';
        console.log('Movie Service initialized.....');
    }
  
    searchMovies(searchStr:string) {
        this.searchURL = 'http://data.tmsapi.com/v1.1/programs/'+searchStr+'?api_key='+this.apikey;
        return this._http.get(this.searchURL)
        .map(res => res.json());
    }

    getMovie(id:string) {
        this.searchURL = 'http://data.tmsapi.com/v1.1/programs/'+id+'?api_key='+this.apikey;
        return this._http.get(this.searchURL)
        .map(res => res.json());
    }
}