import React, { Component } from 'react'
import './Example.css';
import welcome_background from '../../../images/welcome_background.jpg'

import * as Survey from "survey-react";
import "survey-react/survey.css";



class Example extends Component {
    constructor(props){
        super(props);
        
        this.state = {
            testEnabled: this.props.testEnabled,
            setTest: this.props.setTest
        };
    }

    onComplete(survey, options) {
        let answer_to_int = {"Not at All": 0, 
                                "Rarely": 1, 
                                "Sometimes": 2, 
                                "Often": 3, 
                                "Very Often": 4};
        
        let trait_to_question = [[6, 8, 13], [3, 11, 15], [10, 12, 14], [2, 5, 7, 16], [4, 9]]

        let result = []

        let survey_data = JSON.parse(JSON.stringify(survey.data));

        for (let i = 0; i < trait_to_question.length; i++) {
            let temp_score = 0
            for (let j = 0; j < trait_to_question[i].length; j++) {
                let temp_answer = survey_data['question' + trait_to_question[i][j]]
                temp_score = temp_score + answer_to_int[temp_answer]
            }

            temp_score = temp_score / trait_to_question[i].length
            result.push(temp_score);
        }

        console.log(result)

        this.state.setTest(result)
    }

    json = {
        title: "Determine soft skill",
        showProgressBar: "bottom",
        firstPageIsStarted: true,
        startSurveyText: "Start test",

        pages: [
            {
                questions: [
                    {
                        type: "html",
                        html: "Answer 15 questions about your soft skills."
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "I routinely set realistic goals for myself, and I track my progress until I've reached them.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            }, 

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When I have to make a decision, I pick the first good solution I find.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "I approach life with confidence, and I have high self esteem.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When it comes to managing my workload, I know my priorities.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "Team development is an area I admit to cutting back on when time and resources are limited.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "I lose time during the day because I'm not sure what I need to get done.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When I want to motivate people, I try to use the same approach with each person.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "The work I do on a daily basis reflects my values, and is consistent with the goals I've set for myself.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "I'm able to communicate my needs, and I make sure that my message is heard and understood.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When I encounter a problem, I immediately begin looking for potential solutions.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When there's conflict, I use my communication skills to find solutions and work things through.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "I'm aware of the differences between leadership and management.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When discussing an issue with someone, I try to stay one step ahead in the conversation, and I actively think about what I'm going to say next.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "When I encounter a setback, I have difficulty focusing on the situation positively and objectively.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            },

            {
                questions: [
                    {
                        type: "radiogroup",
                        title: "I'm motivated to complete all of my work in a timely manner.",
                        choices: [
                            "Not at All", "Rarely", "Sometimes", "Often", "Very Often"
                        ]
                    }
                ]
            }
        ],

        completedHtml: "Great! Your Tviz waiting for you on next page."
    };

    render() {
        const { testEnabled } = this.state;
        let model = new Survey.Model(this.json);

        if (testEnabled) {
            return (<Survey.Survey model={model} onComplete={this.onComplete}/>);
        }

        return (
                <div className="container image-container">
                    <img src={ welcome_background }/>
                </div>
        );
    }
}

export default Example