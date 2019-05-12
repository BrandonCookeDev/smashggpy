# smashgg.py

**smashgg.py** is an SDK that wraps around the public smash.gg GraphQL API. 
It implements a series of easy to use objects, and features a background thread which
manages outstanding queries to handle GraphQL's Rate Limiting feature.

* Author
    * Brandon Cooke (brandoncookedev@gmail.com)

## Getting Started

```python
from smashgg.py import Initializer, Logger, Event
if __name__ == '__main__':
    Initializer.initialize('API_KEY')
    
    f1_melee = Event.get('function-1', 'melee-singles')
    f1_melee_sets = f1_melee.get_sets()
    for f1_set in f1_melee_sets:
        print("{0}: {1} {2} - {3} {4}".format(
            f1_set.full_round_text,
            f1_set.player1,
            f1_set.score1,
            f1_set.score2,
            f1_set.player2)
        )
```
    
This results in the following:

    
## Docs

### Tournament

#### Properties
* id
    * int 
    * id of the tournament object
* name
    * string 
    * name of the tournament
* slug
    * string 
    * url slug of the tournament
* start_time
    * int 
    * unix epoch of the tournament start time
* end_time
    * int
    * unix epoch of the tournament end time
* timezone
    * string 
    * timezone the tournament took place in
* venue
    * [Venue](#venue)
* organizer
    * [Organizer](#organizer)

#### Methods

##### Static
* parse(data)
    * parse smash.gg api data into a Tournament object
    * parameters
        * data
            * json
            * http response data from a smash.gg api call
    * returns [Tournament](#tournament)
* get_events()
    * get all the events for a given tournament
    * returns [Event](#event)[]
* get_phases()
    * get all the phases for a given tournament
    * returns [Phase](#phase)[]
* get_phase_groups()
    * get all the phase groups for a given tournament
    * returns [PhaseGroup](#phasegroup)[]
* get_attendees()
    * get all the attendees for a given tournament
    * returns [Attendee](#attendee)[]
* get_entrants()
    * get all the entrants for a given tournament
    * returns [Entrant](#entrant)[]  
* get_sets()
    * get all of the sets played for a given tournament
    * returns [GGSet](#ggset)[]
* get_incomplete_sets()
    * get all of the incomplete sets for a given tournament
    * returns [GGSet](#ggset)[]
* get_completed_sets()
    * get all of the completed sets for a given tournament
    * returns [GGSet](#ggset)[]


##### Instance
* get_id
    * get the id property of the tournament
    * returns int
* get_name
    * get the name property of the tournament
    * returns string
* get_slug
    * get the slug property of the tournament
    * returns string
* get_start_time
    * get the start_time property of the tournament
    * returns int
* get_end_time
    * get the end_time property of the tournament
    * returns int
* get_timezone
    * get the timezone property of the tournament 
    * returns string
* get_venue
    * get the venue property of the tournament
    * returns [Venue](#venue)
* get_organizer
    * get the organizer property of the tournament
    * returns [Organizer](#organizer)

### Event

#### Properties

* id
    * int
    * the numeric id of the event
* name
    * string
    * the name of the event
* slug
    * string
    * the url slug of the event
* state
    * string
    * the progress of the event
    * possible values:
        * CREATED
        * ACTIVE
        * COMPLETED
        * READY
        * INVALID
        * CALLED
        * QUEUED
* start_at
    * int
    * unix epoch of the start time of the event
* num_entrants
    * int
    * number of entrants in the event
* check_in_buffer
    * int
    * seconds of how long before the event start will the check-in end
* check_in_duration
    * int
    * seconds of how long the check-in will last
* check_in_enabled
    * bool
    * t/f of whether this event uses check-in
* is_online
    * bool
    * t/f of whether this event is online
* team_name_allowed
    * bool
    * t/f of whether this event allows team names
* team_management_deadline
    * int
    * unix epoch of when team management is no longer allowed

#### Methods

##### Statics
* parse(data) 
    * parse smash.gg api data into an Event object
    * parameters
        * data
            * json
            * http response data from a smash.gg api call
    * returns [Event](#event)
* get_phase()
    * get the phases of the event
    * returns [Phase](#phase)[]
* get_phase_groups()
    * get the phase groups of the event
    * returns [PhaseGroup](#phasegroup)[]
* get_sets()
    * get all of the sets played for a given event
    * returns [GGSet](#ggset)[]
* get_incomplete_sets()
    * get all of the incomplete sets for a given event
    * returns [GGSet](#ggset)[]
* get_completed_sets()
    * get all of the completed sets for a given event
    * returns [GGSet](#ggset)[]

##### Instance
* get_id()
    * get the id property of the event
    * returns int
* get_name()
    * get the name property of the event
    * returns string
* get_slug()
    * get the slug property of the event
    * returns string
* get_state()
    * get the state property of the event
    * returns string
* get_start_at()
    * get the start_at property of the event
    * returns int
* get_num_entrants()
    * get the num_entrants property of the event
    * returns int 
* get_check_in_buffer()
    * get the check_in_buffer property of the event
    * returns int
* get_check_in_duration()
    * get the check_in_duration property of the event
    * returns int
* get_check_in_enabled()
    * get the check_in_enabled property of the event
    * returns bool
* get_is_online()
    * get the is_online property of the event
    * returns bool
* get_team_name_allowed()
    * get the team_name_allowed property of the event
    * returns bool
* get_team_management_deadline()
    * get the team_management_deadline property of the event
    * returns int

### Phase

#### Properties
* id
    * int
    * numeric id of the phase
* name
    * string
    * name of the phase
* num_seeds
    * int
    * number of seeds that are in the phase
* group_count
    * int
    * number of phase groups that are in the phase

#### Methods

##### Statics
* parse(data)
    * parse smash.gg api data into an Phase object
    * parameters
        * data
            * json
            * http response data from a smash.gg api call
    * returns [Phase](#phase)
* get_phase_groups()
    * get the phase groups for the given phase
    * returns [PhaseGroup](#phasegroup)[]
* get_sets()
    * get all of the sets played for the given phase
    * returns [GGSet](#ggset)[]
* get_incomplete_sets()
    * get all of the incomplete sets for the given phase
    * returns [GGSet](#ggset)[]
* get_completed_sets()
    * get all of the completed sets for the given phase
    * returns [GGSet](#ggset)[]

##### Instance
* get_id()
    * get the id property of the Phase
    * returns int
* get_name()
    * get the name property of the Phase
    * returns string 
* get_num_seeds()
    * get the num_seeds property of the Phase
    * returns int
* get_group_count()
    * get the group_count property of the Phase
    * returns int

### PhaseGroup

#### Properties

* id
    * int
    * numeric id of the phase group
* display_identifier
    * string
    * the name of the phase group
* first_round_time
    * int
    * unix epoch of the time the first round of this phase group begins
* state
    * int
    * progress of the phase group
* phase_id
    * int
    * numeric id of the phase this phase group belongs to
* wave_id
    * int
    * numeric id of the wave this phase group belongs to
* tiebreak_order
    * json
    * the tiebreak order for this phase group

#### Methods

##### Statics
* parse(data)
    * parse smash.gg api data into a PhaseGroup object
    * parameters
        * data
            * json
            * http response data from a smash.gg api call
    * returns [PhaseGroup](#phasegroup)
* get_sets()
    * get all of the sets played for the given phase group
    * returns [GGSet](#ggset)[]
* get_incomplete_sets()
    * get all of the incomplete sets for the given phase group
    * returns [GGSet](#ggset)[]
* get_completed_sets()
    * get all of the completed sets for the given phase group
    * returns [GGSet](#ggset)[]

##### Instance
* get_id()
    * get the id property of the phase group
    * returns int
* get_display_identifier()
    * get the display_identifier property of the phase group
    * returns string
* get_first_round_time()
    * get the first_round_time property of the phase group
    * returns int
* get_state()
    * get the state property of the phase group
    * returns int
* get_phase_id()
    * get the phase_id property of the phase group
    * returns int
* get_wave_id()
    * get the wave_id property of the phase group
    * returns int
* get_tiebreak_order()
    * get the tiebreak_order property of the phase group
    * returns json
    
### GGSet

#### Properties
* id
    * int
    * numeric id of the set
* event_id
    * int
    * numeric id of the event this set belongs to
* phase_group_id
    * int
    * numeric id of the phase group this set belongs to
* display_score
    * string
    * display string for this set. 
        * Format: Smashtag1 Score1 - Score2 Smashtag2
* full_round_text
    * string
    * full name of the round this set takes place in
* round
    * int
    * numeric identifier for the round this set takes place in
* started_at
    * int
    * unix epoch of the time this set started at
* completed_at
    * int 
    * unix epoch of the time this set ended at
* winner_id
    * int
    * id number of the of [Entrant](#entrant) who won the set
* total_games
    * int
    * total number of games played in this set
* state
    * int
    * progress of the set
* player1
    * [Player](#player)
    * 1st player in the set
* player2
    * [Player](#player)
    * 2nd player in the set
* score1
    * int
    * score of player 1 in the set
* score2
    * int
    * score of player 2 in the set

#### Methods

##### Statics
* parse(data)
    * parse smash.gg api data into a GGSet object
    * parameters
        * data
            * json
            * http response data from a smash.gg api call
    * returns [GGSet](#ggset)
* parse_display_score(display_score)
    * parse a GGSet's display score property
    * parameters
        * data
            * string
            * display score string from a GGSet object
    * returns custom object:
        * p1_tag
            * string or None
            * smashtag of player 1
        * p1_score
            * int
            * score of player 1
        * p2_tag
            * string or None
            * smashtag of player 2
        * p2_score
            * int
            * score of player 2

##### Instance
* get_id()
    * get the id property of the event
    * returns int
* get_event_id()
    * get the event_id property of the event
    * returns int
* get_phase_group_id()
    * get the phase_group_id property of the event
    * returns int
* get_display_score()
    * get the display_score property of the event
    * returns string
* get_full_round_text()
    * get the full_round_text property of the event
    * returns string
* get_round()
    * get the round property of the event
    * returns int
* get_started_at()
    * get the started_at property of the event
    * returns int
* get_completed_at()
    * get the completed_at property of the event
    * returns int
* get_winner_id()
    * get the winner_id property of the event
    * returns int
* get_total_games()
    * get the total_games property of the event
    * returns int
* get_state()
    * get the state property of the event
    * returns int
* get_player1()
    * get the player1 property of the event
    * returns [Player](#player)
* get_player2()
    * get the player2 property of the event
    * returns [Player](#player)
* get_score1()
    * get the score1 property of the event
    * returns int
* get_score2()
    * get the score2 property of the event
    * returns int

### Player

#### Properties
* tag
    * string
    * smashtag/identifier for this Player
* entrant_id
    * int
    * unique entrant id number for this Player
* attendee_ids
    * int[]
    * array of attendee ids for the attendees who make up this Player

#### Methods

##### Statics
* parse(tag, data)
    * parse smash.gg api data into a Player object 
    * parameters
        * tag
            * string
            * smashtag of the player
        * data
            * json
            * data from smashgg to be parsed into entrant and attendee ids
    * returns [Player](#player)

##### Instance
* get_tag()
    * get the tag property of this player
    * returns string
* get_entrant_id()
    * get the entrant_id property of this player
    * returns int
* get_attendee_ids()
    * get the attendee_ids property of this player
    * returns int[]

## How to run

**NOTE:** In order to use properly, you will need to create an .env file with the API_TOKEN inside of it, it should look like this: 
`API_TOKEN=<insert smash.gg API token here>`
If you already have Docker installed, you may run the scripts in the /docker directory.
You need to build the container before running it, so run `build` before `run`.
If you would like to do both consecutively, you may run the `buildAndRun` script.