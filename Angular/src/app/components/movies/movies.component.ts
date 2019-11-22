import { Component, Input } from '@angular/core';
import { MovieService} from '../../services/movie.service';
import { Http } from '@angular/http';

@Component({
  moduleId: module.id,
  selector: 'movies',
  templateUrl: 'movies.component.html',
})

export class MoviesComponent  {  
    popularList:Array<Object>;
    title:string;
    description:string;
    searchStr:string;
    searchRes:Array<Object>;
    casts:Array<Object>;
    id:string;
    fileName:string;

    constructor(private _movieService:MovieService) {
        
    }

    uploadFile(event: { target: any; }) {
        let elem = event.target;
        if(elem.files.length > 0) {
            this.fileName = elem.files[0].name.split('.')[0]; 
            this.searchMovies(this.fileName);
        }
    }

    searchMovies(fileName:string) {
        this._movieService.searchMovies(fileName).subscribe( res => {
            console.log(res);
            this.id = res.rootId;
            this.title = res.title;
            this.description = res.longDescription;
            this.casts = res.cast;
            this.searchRes = res;
        });
    }
}