import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';

import {MovieService} from '../../services/movie.service';

@Component({
    moduleId: module.id,
    selector: 'movie',
    templateUrl: 'movie.component.html',
    styleUrls: ['movie.component.css']
  })

  export class MovieComponent implements OnInit{
      movie:Object;
      rootid:string;

      constructor(
          private router:ActivatedRoute,
          private _movieService:MovieService){

          }

        ngOnInit() {
            this.router.params.subscribe((params) => {
                let id = params['id'];
                this.rootid = params['id'];
                this._movieService.getMovie(id).subscribe(movie => {
                    console.log(movie);
                });
            });
        }
  }

