# My first project

- ბიბლიოთეკის პროგრამა
- კინოთეატრის პროგრამა - გაიმარჯვა
- საქმეების მართვის პროგრამა
- ექსჩეინჯების პროგრამა
- პირადი ელექტრონული საფულე
- სოციალური ქსელი
- თავისუფალი მეგობრების შეხვედრის შემთავაზებელი
- გაცნობა-დაოჯახების პროგრამა
- ფლეშქარდების პროგრამა
- თამაში: ჩაძირობანა
- თამაში: მგელობანა
- სახეების ამომცნობი
- სახეების დამმალავი

---

- Web
- Desktop
- Mobile
- CLI - command line interface

PO - Product owner - ირაკლი

## Abstract

We are building CLI application to manage tickets for cinema. Application should bring possibility to users to see available places and book tickets. We need to have Admin user which can manage everything. 

## User Stories

When user enters in system, should be able to search for specific movie. After successful search, program should display all sessions. 

When program starts, it should display menu items.

 1. list sessions

 2. search movie

1. my tickets
2. admin

When admin signs in, should be able to see menu items

1. list all sessions 
2. remove session
3. add session
4. edit session (only increase room size)

## Requirements

Program should be able to handle 100 000 000 sessions. 

Search performance must be less than 100 ms. 

If there is not exact match, then program should display fuzzy search results

## Technical Implementation

We should use functions and try to create reusable functions. We should store info in dictionaries and lists. 

Users will interact using CLI. 

There will be main function which will control program lifecycle. To increase readability we will distribute functionality into multiple files. 

During search we will use - Levenshtein distance

## Diagram

TBD