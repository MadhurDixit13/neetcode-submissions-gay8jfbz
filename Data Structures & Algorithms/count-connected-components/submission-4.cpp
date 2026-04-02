class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        map<int, vector<int>> m;
        map<int, bool> visited;
        int ans=0;
        if(edges.size() == 0){
            return n;
        }
        for(auto i: edges){
            m[i[0]].push_back(i[1]);
            m[i[1]].push_back(i[0]);
        }
        for(int i = 0; i<n; i++){
            visited[i] = false;
        }
        
        for(auto i : visited){
            queue<int> q;
            if(!i.second){
                q.push(i.first);
                visited[i.first] = true;
                ans+=1;
            }
            while(!q.size()==0){
                int temp = q.front();
                for(auto x: m[temp]){
                    if(!visited[x]){
                        q.push(x);
                        visited[x] = true;
                    }   
                }
                q.pop();
            }
        }
        return ans;
    }
};
