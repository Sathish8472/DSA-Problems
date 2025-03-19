class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        num_teams = len(votes[0])

        vote_count = {team: [0] * num_teams for team in votes[0]}

        for vote in votes:
            for rank, team in enumerate(vote):
                #print(f"rank: {rank}, team: {team}")
                vote_count[team][rank] += 1
            
        
        # print("vote count: ", vote_count)
        teams = list(vote_count.keys())
        # print(f"Teams: {teams}")

        teams.sort(key = lambda team: (vote_count[team], -ord(team)), reverse=True)

        print(teams)
        return "".join(teams)

        