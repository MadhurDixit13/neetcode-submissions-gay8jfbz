class Solution {
public:
    void bfs(int i, int j, vector<vector<bool>>& visited, vector<vector<int>>& grid, int count) {
        queue<pair<int, int>> q;
        visited[i][j] = true;
        q.push({i, j});
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        while (!q.empty()) {
            int size = q.size();  // To process level by level
            for (int k = 0; k < size; ++k) {
                pair<int, int> temp = q.front();
                q.pop();
                int x = temp.first;
                int y = temp.second;
                
                for (auto dir : directions) {
                    int newX = x + dir.first;
                    int newY = y + dir.second;
                    if (newX >= 0 && newX < grid.size() && newY >= 0 && newY < grid[0].size() && 
                        grid[newX][newY] > count && grid[newX][newY] != -1) {
                        q.push({newX, newY});
                        grid[newX][newY] = count + 1;
                        visited[newX][newY] = true;
                    }
                }
            }
            count++;
        }
    }

    void islandsAndTreasure(vector<vector<int>>& grid) {
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
        
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 0 && !visited[i][j]) {
                    bfs(i, j, visited, grid, 0);
                }
            }
        }
    }
};
