import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const TABS = ['Weekly', 'All Time', 'Friends'];

const LEADERBOARD_DATA = {
  Weekly: [
    { id: 1, name: 'Priya Sharma', xp: 2840 },
    { id: 2, name: 'Raj Patel', xp: 2720 },
    { id: 3, name: 'Anita Gupta', xp: 2590 },
    { id: 4, name: 'Vikram Singh', xp: 2450 },
    { id: 5, name: 'Deepa KC', xp: 2310 },
    { id: 6, name: 'Sujan Thapa', xp: 2180 },
    { id: 7, name: 'Maya Devi', xp: 2050 },
    { id: 8, name: 'Kiran Joshi', xp: 1920 },
    { id: 9, name: 'Rohit Shrestha', xp: 1790 },
    { id: 10, name: 'Sita Rai', xp: 1660 },
    { id: 11, name: 'Binod Bhandari', xp: 1530 },
    { id: 12, name: 'Gita Adhikari', xp: 1400 },
    { id: 13, name: 'Hari Khatri', xp: 1270 },
    { id: 14, name: 'Laxmi Poudel', xp: 1140 },
    { id: 15, name: 'Nabin (You)', xp: 1100, isCurrentUser: true },
  ],
  'All Time': [
    { id: 1, name: 'Raj Patel', xp: 15800 },
    { id: 2, name: 'Priya Sharma', xp: 14200 },
    { id: 3, name: 'Anita Gupta', xp: 13900 },
    { id: 4, name: 'Vikram Singh', xp: 12700 },
    { id: 5, name: 'Deepa KC', xp: 11300 },
    { id: 6, name: 'Sujan Thapa', xp: 10400 },
    { id: 7, name: 'Maya Devi', xp: 9900 },
    { id: 8, name: 'Kiran Joshi', xp: 8500 },
    { id: 9, name: 'Rohit Shrestha', xp: 7200 },
    { id: 10, name: 'Sita Rai', xp: 6800 },
    { id: 11, name: 'Binod Bhandari', xp: 5400 },
    { id: 12, name: 'Gita Adhikari', xp: 4200 },
    { id: 13, name: 'Hari Khatri', xp: 3100 },
    { id: 14, name: 'Laxmi Poudel', xp: 2900 },
    { id: 15, name: 'Nabin (You)', xp: 2700, isCurrentUser: true },
  ],
  Friends: [
    { id: 1, name: 'Priya Sharma', xp: 2840, isFriend: true },
    { id: 2, name: 'Anita Gupta', xp: 2590, isFriend: true },
    { id: 3, name: 'Nabin (You)', xp: 1100, isCurrentUser: true },
    { id: 4, name: 'Sujan Thapa', xp: 2180, isFriend: true },
    { id: 5, name: 'Rohit Shrestha', xp: 1790, isFriend: true },
  ],
};

const LeaderboardScreen = () => {
  const [activeTab, setActiveTab] = useState('Weekly');
  const data = LEADERBOARD_DATA[activeTab] || [];

  const getRankIcon = (rank) => {
    if (rank === 1) return { name: 'trophy', color: '#FFD700' };
    if (rank === 2) return { name: 'medal', color: '#C0C0C0' };
    if (rank === 3) return { name: 'ribbon', color: '#CD7F32' };
    return null;
  };

  const renderItem = ({ item, index }) => {
    const rank = index + 1;
    const rankIcon = getRankIcon(rank);
    const isCurrentUser = item.isCurrentUser;

    return (
      <View
        style={[
          styles.leaderboardRow,
          isCurrentUser && styles.currentUserRow,
        ]}
      >
        <View style={styles.rankContainer}>
          {rankIcon ? (
            <Ionicons name={rankIcon.name} size={24} color={rankIcon.color} />
          ) : (
            <Text style={styles.rankText}>{rank}</Text>
          )}
        </View>
        <View style={styles.avatar}>
          <Ionicons
            name="person-circle"
            size={40}
            color={isCurrentUser ? '#6C63FF' : '#bbb'}
          />
        </View>
        <View style={styles.userInfo}>
          <Text
            style={[
              styles.userName,
              isCurrentUser && styles.currentUserName,
            ]}
          >
            {item.name}
          </Text>
          <Text style={styles.xpText}>{item.xp} XP</Text>
        </View>
        {isCurrentUser && (
          <View style={styles.youBadge}>
            <Text style={styles.youBadgeText}>You</Text>
          </View>
        )}
      </View>
    );
  };

  const currentUserRank = data.findIndex(item => item.isCurrentUser) + 1;
  const totalPlayers = data.length;

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Leaderboard</Text>
        <View style={styles.tabContainer}>
          {TABS.map(tab => (
            <TouchableOpacity
              key={tab}
              style={[
                styles.tab,
                activeTab === tab && styles.activeTab,
              ]}
              onPress={() => setActiveTab(tab)}
            >
              <Text
                style={[
                  styles.tabText,
                  activeTab === tab && styles.activeTabText,
                ]}
              >
                {tab}
              </Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>

      <View style={styles.yourRankCard}>
        <Ionicons name="trophy" size={20} color="#6C63FF" />
        <Text style={styles.yourRankText}>
          Your Rank: #{currentUserRank} of {totalPlayers}
        </Text>
      </View>

      <FlatList
        data={data}
        keyExtractor={item => item.id.toString()}
        renderItem={renderItem}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.listContainer}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F7F7F7',
  },
  header: {
    backgroundColor: '#6C63FF',
    paddingTop: 50,
    paddingBottom: 20,
    paddingHorizontal: 20,
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 16,
  },
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 10,
    padding: 4,
  },
  tab: {
    flex: 1,
    paddingVertical: 8,
    alignItems: 'center',
    borderRadius: 8,
  },
  activeTab: {
    backgroundColor: '#fff',
  },
  tabText: {
    color: '#ddd',
    fontWeight: '600',
  },
  activeTabText: {
    color: '#6C63FF',
  },
  yourRankCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#fff',
    marginHorizontal: 16,
    marginTop: 16,
    marginBottom: 8,
    padding: 12,
    borderRadius: 10,
    elevation: 1,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 3,
  },
  yourRankText: {
    marginLeft: 8,
    fontSize: 14,
    color: '#6C63FF',
    fontWeight: '600',
  },
  listContainer: {
    paddingHorizontal: 16,
    paddingBottom: 20,
  },
  leaderboardRow: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 12,
    borderRadius: 10,
    marginBottom: 8,
    elevation: 1,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 3,
  },
  currentUserRow: {
    backgroundColor: '#F0EFFF',
    borderWidth: 1,
    borderColor: '#C4B5FD',
  },
  rankContainer: {
    width: 30,
    alignItems: 'center',
    justifyContent: 'center',
  },
  rankText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#666',
  },
  avatar: {
    marginLeft: 8,
  },
  userInfo: {
    flex: 1,
    marginLeft: 12,
  },
  userName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
  },
  currentUserName: {
    color: '#6C63FF',
  },
  xpText: {
    fontSize: 13,
    color: '#888',
    marginTop: 2,
  },
  youBadge: {
    backgroundColor: '#6C63FF',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  youBadgeText: {
    color: '#fff',
    fontSize: 12,
    fontWeight: 'bold',
  },
});

export default LeaderboardScreen;