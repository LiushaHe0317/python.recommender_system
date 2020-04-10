import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements OnInit {
  configUrl = "http://localhost:5000/predict/" + 1;
  fetchedRecipe = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getRecommendations();
  }

  getRecommendations() {
    this.http.get(this.configUrl).subscribe(
      (response: any[]) => this.fetchedRecipe = response,
      (error) => console.log(error)
    );
  }
}
